import asyncio
from datetime import datetime, timedelta
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from kasa import SmartPlug

from plugs.PlugController import PlugController


class PlugConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.plug_controller = PlugController()
        # Asegurarte de inicializar el estado del enchufe
        await self.plug_controller.update_plug()
        self.task = asyncio.create_task(self.send_plug_data())

    async def disconnect(self, close_code):
        self.task.cancel()

    async def send_plug_data(self):
        while True:
            await self.plug_controller.update_plug()
            end_date = datetime.now() - timedelta(days=1)

            emeter_today = await self.plug_controller.plug_emeter_today()
            total_seven_day_consumption = await self.plug_controller.plug_total_consumption(start_date=end_date - timedelta(days=7), end_date=end_date)
            total_thirty_day_consumption = await self.plug_controller.plug_total_consumption(start_date=end_date - timedelta(days=30), end_date=end_date)

            data = {
                'today_energy_cost': self.plug_controller.energy_cost(emeter_today),
                'seven_day_energy_cost': self.plug_controller.energy_cost(total_seven_day_consumption),
                'thirty_day_energy_cost': self.plug_controller.energy_cost(total_thirty_day_consumption),
                'current_consumption': await self.plug_controller.plug_current_consumption(),
                'total_consumption': emeter_today,
                'average_seven_day_consumption': round((total_seven_day_consumption / 7), 2),
                'total_seven_day_consumption': total_seven_day_consumption,
                'average_thirty_day_consumption': round((total_thirty_day_consumption / 30), 2),
                'total_thirty_day_consumption': total_thirty_day_consumption,
                'usage_today': await self.plug_controller.plug_usage_today()
            }
            await self.send(text_data=json.dumps(data))
            await asyncio.sleep(3)

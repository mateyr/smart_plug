import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
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

            emeter_today = await self.plug_controller.plug_emeter_today()
            total_seven_day_consumption = await self.plug_controller.plug_total_seven_day_consumption()
            total_thirty_day_consumption = await self.plug_controller.plug_total_thirty_day_consumption()

            today_energy_cost = self.plug_controller.energy_cost(emeter_today)
            seven_day_energy_cost = self.plug_controller.energy_cost(
                total_seven_day_consumption)
            thirty_day_energy_cost = self.plug_controller.energy_cost(
                total_thirty_day_consumption)

            data = {
                'today_energy_cost': today_energy_cost,
                'seven_day_energy_cost': seven_day_energy_cost,
                'thirty_day_energy_cost': thirty_day_energy_cost,
                'current_consumption': await self.plug_controller.plug_current_consumption(),
                'total_consumption': emeter_today,
                'average_seven_day_consumption': await self.plug_controller.plug_average_seven_day_consumption(),
                'total_seven_day_consumption': total_seven_day_consumption,
                'average_thirty_day_consumption': await self.plug_controller.plug_average_thirty_day_consumption(),
                'total_thirty_day_consumption': total_thirty_day_consumption,
                'usage_today': await self.plug_controller.plug_usage_today()
            }
            await self.send(text_data=json.dumps(data))
            await asyncio.sleep(3)

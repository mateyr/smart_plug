import asyncio
from datetime import datetime, timedelta
from kasa import SmartPlug, Discover


class PlugController():

    def __init__(self):
        # plug = self.discover_plugs(plug_name)
        self.plug = SmartPlug("192.168.1.31")

    # def discover_plugs(self):
    #     # plug = []
    #     # found_device = asyncio.run(Discover.discover())
    #     # ip_address = [found_device]
    #     # for count, device in enumerate(found_device.values()):
    #     #   if device.is_plug:
    #     #     plug.append(ip_address[count])
    #     plug = SmartPlug("192.168.1.26")
    #     return plug

    # General
    async def update_plug(self):
        await self.plug.update()

    async def plug_off(self):
        await self.update_plug()
        await self.plug.turn_off()

    async def plug_on(self):
        await self.update_plug()
        await self.plug.turn_on()

    # Energy Cost
    def energy_cost(self, energy):
        return round(energy * 9, 2)

    # Energy usage
    async def plug_current_consumption(self):
        await self.update_plug()
        current_consumption = await self.plug.current_consumption()
        return round(current_consumption, 2)

    async def plug_emeter_today(self):
        await self.update_plug()
        return round(self.plug.emeter_today, 2)

    async def plug_total_consumption(self, start_date: datetime, end_date: datetime):
        await self.update_plug()
        total_consumption = await self.plug.get_emeter_total_consumption(start_date=start_date, end_date=end_date)
        return round(total_consumption, 2)

    async def plug_usage_today(self):
        await self.update_plug()
        usage = self.plug.modules["usage"]
        usage_today = usage.usage_today / 60
        return round(usage_today, 2)

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

    async def general_info(self):
        await self.plug.update()

        alias = self.plug.alias
        time = self.plug.time
        model = self.plug.model
        hw_version = self.plug.hw_info['hw_ver']

        return {'alias': alias, 'device_time': time, 'model': model, 'hardware_version': hw_version}

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

        total_consumption = 0
        current_date = start_date
        while current_date <= end_date:
            raw_data = await self.plug.get_emeter_daily(year=current_date.year, month=current_date.month)
            data = raw_data.get(current_date.day)
            if data is not None:
                total_consumption += data

            current_date += timedelta(days=1)
        return round(total_consumption, 2)

    # Execution time
    async def plug_usage_today(self):
        await self.update_plug()
        usage = self.plug.modules["usage"]
        usage_today = usage.usage_today / 60
        return round(usage_today, 2)

    async def plug_total_usage(self, start_date: datetime, end_date: datetime):
        await self.update_plug()
        usage = self.plug.modules["usage"]
        total_usage = 0
        current_date = start_date
        while current_date <= end_date:
            raw_data = await usage.get_daystat(year=current_date.year, month=current_date.month)
            data = raw_data.get(current_date.day)
            if data is not None:
                total_usage += data

            current_date += timedelta(days=1)
        total_usage = total_usage / 60
        return round(total_usage, 2)

    # Historial
    async def plug_emeter_monthly(self):
        await self.update_plug()
        emeter_monthly = await self.plug.get_emeter_monthly()

        return emeter_monthly

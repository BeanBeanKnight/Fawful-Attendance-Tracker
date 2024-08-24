from .attendance_tracker_cog import AttendanceTrackerCog


async def setup(bot):
    await bot.add_cog(AttendanceTrackerCog(bot))
    print('Cog loaded: AttendanceTrackerCog')

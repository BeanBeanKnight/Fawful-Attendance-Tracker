from redbot.core import commands

class AttendanceTrackerCog(commands.Cog):
    """Attendance Tracker Cog"""

    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def start_event(self, ctx):
            """Start the attendance tracker"""
            # code goes here
            await ctx.send('Attendance Tracker Started')

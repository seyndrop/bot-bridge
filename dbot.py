import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.slash_command(name="start", description="Запустить")
async def start(interaction: nextcord.Interaction):
    await interaction.response.send_message("complete")

bot.run("DISCORD_TOKEN")
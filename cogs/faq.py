import disnake
from disnake.ext import commands

class Links(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(
            disnake.ui.Button(
                label="GitHub Repo",
                url="https://github.com/EQUENOS/disnake"
            )
        )
        self.add_item(
            disnake.ui.Button(
                label="Docs",
                url="https://disnake.readthedocs.io/en/latest/"
            )
        )
        self.add_item(
            disnake.ui.Button(
                label="Examples",
                url="https://github.com/EQUENOS/disnake/tree/master/examples"
            )
        )

class Faq(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="faq",
        description="See the most frequently asked questions"
    )
    async def faq(self, interaction):
        embed=disnake.Embed(
            title="FAQ",
            color=disnake.Color.gold()
        )
        embed.add_field(
            name="- Does disnake have slash commands?",
            value="Yes, it is completely up to date with Discord. It has all interactions (such as buttons and select menus) and application commands (slash commands and context menus).\n([Click here to learn how learn how to create a slash command using disnake](https://disnake.readthedocs.io/en/latest/ext/commands/slash_commands.html#slash-commands))",
            inline=False
        )
        embed.add_field(
            name="- How do I switch to disnake?",
            value="Simply install disnake using `pip install disnake`. But don't forget to remove discord.py. Your discord.py code will still work with disnake if it was written in discord.py 2.0. Use this to install the development version: ```py\npip install -U git+https://github.com/EQUENOS/disnake\n```",
            inline=False
        )
        embed.add_field(
            name="- Why aren't my slash commands being registered?",
            value="There can be several reasons why slash commands aren't being registered, the main one being that your slash command is global. Global slash commands register to all guilds and can take upto an hour. If you want to register the slash command just to one or a few guilds, use [`guild_ids`](https://disnake.readthedocs.io/en/latest/ext/commands/api.html?#disnake.ext.commands.InvokableSlashCommand.guild_ids) in your slash command decorator to register the slash command register only to the specified guilds. Using [`test_guilds`](https://disnake.readthedocs.io/en/latest/ext/commands/api.html?#disnake.ext.commands.Bot.test_guilds) in your bot instance will register all of your slash commands only to those specified guilds.",
            inline=False
        )
        embed.add_field(
            name="- How do I respond to an interacton?",
            value="Interactions use [`disnake.ApplicationCommandInteraction`](https://disnake.readthedocs.io/en/latest/api.html?#disnake.ApplicationCommandInteraction) instead of `ctx` (which can be shortened to `inter` as well).\nAn interaction response can be created using [`Interaction.response`](https://disnake.readthedocs.io/en/latest/api.html?#disnake.Interaction.response) followed by [`disnake.InteractionResponse`](https://disnake.readthedocs.io/en/latest/api.html?#disnake.InteractionResponse).\nSimple example that responds with `Hello!` in an ephemeral message: ```py\nawait interaction.response.send_message(\"Hello!\", ephemeral=True)\n```",
            inline=False
        )

        await interaction.response.send_message(embed=embed, view=Links())

def setup(bot):
    bot.add_cog(Faq(bot))

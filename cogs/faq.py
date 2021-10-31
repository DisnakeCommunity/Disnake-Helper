import disnake
from disnake.ext import commands
from disnake.ext.commands import Param

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


faq=[
    {
        "question" : "Does disnake have slash commands?",
        "answer" : "Yes, it is completely up to date with Discord. It has all interactions (such as buttons and select menus) and application commands (slash commands and context menus).\n([Click here to learn how learn how to create a slash command using disnake](https://disnake.readthedocs.io/en/latest/ext/commands/slash_commands.html#slash-commands))"
    },
    {
        "question" : "How do I switch to disnake?",
        "answer" : "Simply install disnake using `pip install disnake`. But don't forget to remove discord.py. Your discord.py code will still work with disnake if it was written in discord.py 2.0. Use this to install the development version: ```py\npip install -U git+https://github.com/EQUENOS/disnake\n```"
    },
    {
        "question" : "Why can't I see my slash commands?",
        "answer" : "There can be several reasons why slash commands aren't being registered, the main one being that your slash command is global. Global slash commands register to all guilds and can take upto an hour. If you want to register the slash command just to one or a few guilds, use [`guild_ids`](https://disnake.readthedocs.io/en/latest/ext/commands/api.html?#disnake.ext.commands.InvokableSlashCommand.guild_ids) in your slash command decorator to register the slash command register only to the specified guilds. Using [`test_guilds`](https://disnake.readthedocs.io/en/latest/ext/commands/api.html?#disnake.ext.commands.Bot.test_guilds) in your bot instance will register all of your slash commands only to those specified guilds."
    },
    {
        "question" : "How do I respond to an interacton?",
        "answer" : "Interactions use [`disnake.ApplicationCommandInteraction`](https://disnake.readthedocs.io/en/latest/api.html?#disnake.ApplicationCommandInteraction) instead of `ctx` (which can be shortened to `inter` as well).\nAn interaction response can be created using [`Interaction.response`](https://disnake.readthedocs.io/en/latest/api.html?#disnake.Interaction.response) followed by [`disnake.InteractionResponse`](https://disnake.readthedocs.io/en/latest/api.html?#disnake.InteractionResponse).\nSimple example that responds with `Hello!` in an ephemeral message: ```py\nawait interaction.response.send_message(\"Hello!\", ephemeral=True)\n```"
    }
]


class Faq(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def autocomplete_faq(interaction: disnake.ApplicationCommandInteraction, string: str):
        return list(
            filter(
                lambda question: string in question,
                [i["question"] for i in faq]
            )
        )


    @commands.slash_command(
        name="faq",
        description="See the most frequently asked questions"
    )
    async def faq(self, interaction,
        question: str=Param(description="Your question here", autocomplete=autocomplete_faq)
    ):
        if question in [i["question"] for i in faq]:
            embed=disnake.Embed(
                title=f"FAQ: {question}",
                description=[i["answer"] for i in faq if i["question"] == question][0],
                color=disnake.Color.gold()
            )
            await interaction.response.send_message(embed=embed, view=Links())

        else:
            await interaction.response.send_message("Question not found. Feel free to ask your question in one of the channels though.", ephemeral=True)


def setup(bot):
    bot.add_cog(Faq(bot))

class Script(object):

    START_MSG = """<b>👋🏻Hey {},

I'm an advanced filter bot with many capabilities!
There is no practical limits for my filtering capacity :)

See <i>/help</i> for commands and more details.</b>
"""


    HELP_MSG = """
<i>Add me as admin in your group and start filtering :)</i>
<b>Basic Commands:</b>
/start - Check if I'm alive!
/help - Command help
/about - Something about me!

<b>Filter Commands:</b>
<code>/add</code> name reply  -  Add filter for name
<code>/del</code> name  -  Delete filter
<code>/delall</code>  -  Delete entire filters (Group Owner Only!)
<code>/viewfilters</code>  -  List all filters in chat

<b>Connection Commands:</b>
<code>/connect</code> groupid  -  Connect your group to my PM. 
You can also simply use, <code>/connect</code> in groups.
<code>/connections</code>  -  Manage your connections.

<b>Extras;</b>
/status  -  Shows current status of your bot (Auth User Only)
/id  -  Shows ID information
<code>/info</code> userid  -  Shows User Information. Use <code>/info</code> as reply to some message for their details!

"""


    ABOUT_MSG = """⭕️<b>My Name : Mulgi</b>

⭕️<b>Creater :</b> @HalkatManus    

⭕️<b>Language :</b> <code>Python3</code>

⭕️<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

"""

# PinkSeaMobile
Userstyle and userscript combo to improve drawing on PinkSea from mobile devices.

## Installation
First and foremost, keep in mind you **need BOTH the userstyle AND userscript.**
They are designed to work together and your experience is going to be way clunkier by using the userstyle alone.

With that out of the way - something you'll need regardless of installation method is an userstyle and userscript manager, such as [Stylus](https://add0n.com/stylus.html) and [Tampermonkey](https://www.tampermonkey.net/) respectively.

You do have a couple different ways to install the userstyle+userscript themselves, though.

### UserStyles.world + Greasyfork (easiest, recommended)
The quickest way is to just install them both from [UserStyles](https://userstyles.world/style/20286/pinkseamobile) and [Greasyfork](https://greasyfork.org/en/scripts/523400-pinkseamobile-userscript).

### Building
You should only really need this if you want to tinker with or expand this project.

To build the userstyle, you'll need:
* `ruby-sass`
* `python3`

Clone this repository, and run `build.py`.
The output userstyle will appear at the root of the cloned repository.

At this point, just install that, together with the userscript, through your userstyle and userscript managers.

## Fugue Icons
This userstyle makes use of [Yusuke Kamiyamane's Fugue icons](https://p.yusukekamiyamane.com/), licensed under a [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/).

The specific ones used by PinkSeaMobile are located inside of `style_src/assets/`.


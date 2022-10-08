This repository is an adaptation of [gruvbox theme](https://github.com/morhetz/gruvbox) with Ukrainian palette for [iTerm](https://github.com/gnachman/iTerm2) presets.
Also here you can find a script which is automates dynamically switching between light and dark presets, gruvbox wallpapers, and title bar icon.
## Light theme
![light](https://user-images.githubusercontent.com/79169736/194711213-604367dd-3bd0-4dc5-a4ef-8b9efc1a51ec.png)
![light_ide](https://user-images.githubusercontent.com/79169736/194711242-c888aa72-3857-407b-8e46-5c87181d71ff.png)
## Dark theme
![dark](https://user-images.githubusercontent.com/79169736/194711230-9076d1b4-9ee5-43e5-9db5-d3b22c073f11.png)
![dark_ide](https://user-images.githubusercontent.com/79169736/194711234-df985469-fcef-4b36-9336-7db126ab7b19.png)

## Installation guide

```sh
git clone https://github.com/curiousvlxd/gruvbox-ua-iterm
```
- Go to iTerm > Preferences > Profiles > Colors > Color Presets
- Expand it, click Import and choose color scheme from the presets folder.
- Then go to Appearance > General > Theme and choose Minimal
- Enjoy!

You can also set custom icon:
![title_bar](https://user-images.githubusercontent.com/79169736/194714120-8f7c9651-c828-4ba4-a0fa-c5b7c32b8b97.png)
Go to iTerm > Preferences > Profiles > Icon > Custom and select your one or [which is in the repository.](https://github.com/curiousvlxd/gruvbox-ua-iterm/blob/main/icon.png)

## Dynamic presets
After all manipulations above, I guess you want to sync up with your OS theme.
We have such a script, which is going to be runned by iTerm automatically in the background.
But before that, you need to allow Python API:
![pythonapi](https://user-images.githubusercontent.com/79169736/194715570-6084f98d-38d7-49f4-b373-dd073158eaff.png)
Now you can open Scripts and put here ``Automation`` folder from the repository:
![scripts](https://user-images.githubusercontent.com/79169736/194714637-d1d2fd28-145d-48b1-9562-410d445d803f.png)
Reload iTerm and have fun.
## Dynamic wallpapers
Install [Dynamic Dark Mode](https://github.com/ApolloZhu/Dynamic-Dark-Mode):
```sh
brew install --cask dynamic-dark-mode
```
Open it, go to Configure Dynamic Wallpapers and choose your wallpapers.
Done!








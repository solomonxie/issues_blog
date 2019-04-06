# Vim成长之路
## 学vim的笔记。觉得这样历程型的笔记再好不过了。


VIM Plugins TODO:
- [ ] https://github.com/devjoe/vim-codequery
- [ ] https://github.com/easymotion/vim-easymotion
- [ ] https://github.com/justinmk/vim-sneak
- [ ] https://github.com/sheerun/vim-polyglot
- [ ] https://github.com/wellle/targets.vim
- [ ] https://github.com/ajh17/VimCompletesMe
- [ ] https://github.com/SidOfc/mkdx


## Plugins

### UI

- Start Screen
    - `mhinz/vim-startify`
- Theme
    - `morhetz/gruvbox`
- STATUS-BAR
    - `vim-airline/vim-airline`
    - `vim-airline/vim-airline-themes`
- Syntax Highlighting
    - `hdima/python-syntax`   "Most stable highlighting
- Window
    - `TaDaa/vimade`  "Dim inactive windows
    - `vim-scripts/ZoomWin` "Zoom In/Out (Error)
    - `dhruvasagar/vim-zoom`
    - `junegunn/goyo.vim`  "Focus Mode



### EDIT

- Autocomplete
    - [Snippets]  - Python required
        - `SirVer/ultisnips`  " Track the engine.
        - `honza/vim-snippets`  " Snippets are separated from the engine.
    - [Deoplete]
        - `Shougo/deoplete.nvim`
        - `zchee/deoplete-jedi`    " Python completion source
        - `Shougo/deoplete-clangx`   " C/C++ completion source
- Comment
    - `scrooloose/nerdcommenter`
- Code Check
    - `vim-syntastic/syntastic` "Static Code Check
- Bracket Closing
    - `jiangmiao/auto-pairs` "Smartest (bug:)
- Indentation
    - Plug  'Yggdroot/indentLine'    "Beautiful indent lines
- Trailing Whitespace
    - `bronson/vim-trailing-whitespace`



### Navigation

- Fuzzy File Search
    - fzf
        - `junegunn/fzf`
        - `junegunn/fzf.vim`
    - NetRW
        - `tpope/vim-vinegar`      "Netrw enhancement
- NERDTREE
    - `scrooloose/nerdtree`          " File tree manager
    - `jistr/vim-nerdtree-tabs'      " enhance nerdtree`s tabs
    - `ryanoasis/vim-devicons`       " add beautiful icons besides files
- Bookmarks
    - `MattesGroeger/vim-bookmarks`  "Manage bookmarks
- nnn
    - `mcchrish/nnn.vim`
- Ranger
    - `francoiscabrol/ranger.vim`
- History
    - `yegappan/mru`
- Tags (ctags required)
    - `majutsushi/tagbar`   "Display
    - `ludovicchabant/vim-gutentags` "Manage tags (auto)
    - `craigemery/vim-autotag`  "Navigate (manually gen tags)
- Git
    - `jreybert/vimagit`  "Much easier with Git
    - `tpope/vim-fugitive` "work with fzf for :Commits
    - `iberianpig/tig-explorer.vim` "faster/prettier (tig required)
- Documentation
    - `powerman/vim-plugin-viewdoc` "K-preview improvement


## MISC

- `kassio/neoterm`
- `tpope/vim-obsession`  "For Tmux to restore VIM sessions
- `mbbill/undotree`
- `tweekmonster/startuptime.vim`   "VIM loading analysis


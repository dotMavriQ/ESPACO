![Espaco Logo](https://github.com/dotMavriQ/ESPACO/blob/main/logo.png?raw=true)

![Screenshot](https://github.com/dotMavriQ/ESPACO/blob/main/screenshot.png?raw=true)

Espaço is an Asteroids-like game written in Python using the PyGame library. It provides an exciting space-themed gaming experience where players control a spaceship, navigate through asteroid fields, and destroy asteroids to earn points. The game is currently in the early stages of development (Alpha version) and will be continuously improved over time.

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [TODO List](#todo-list)
- [Contributing](#contributing)
- [License](#license)
- [Special Thanks](#special-thanks)

## Installation

To install and run Espaço on your local machine, follow these steps:

1. Ensure you have Python 3.x installed on your system. If not, you can download it from the official Python website: [python.org/downloads](https://www.python.org/downloads/).

2. Clone this repository to your local machine or download the source code as a ZIP file.

3. Open a terminal or command prompt and navigate to the project directory.

4. Install the required dependencies by running the following command:

```
pip install pygame
```

This will install the PyGame library, which is necessary to run the game.

## Usage

To launch Espaço and start playing, follow these instructions:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command:

```
python asteroids.py
```

3. The game window will appear, and you can use the following controls to play:

- **Arrow Keys**: Move the spaceship.
- **Spacebar**: Shoot bullets.

4. Aim your spaceship at the asteroids and shoot them to earn points. Be careful not to collide with the asteroids, as it will result in damage to your spaceship.

5. The game will continue until your spaceship's health reaches zero. A Game Over screen will be implemented in a future update.

## TODO List

The following tasks are planned for future development of Espaço:

- [ ] Make health work and introduce a Game Over screen.
- [ ] Improve rotation mechanic for the spaceship. Currently, only UP, RIGHT, and SHOOT work correctly, while UP, LEFT, and SHOOT do not function as expected.
- [ ] Limit the splitting of asteroids after a certain point.
- [ ] Enhance the appearance and trajectory of asteroids when hit by a bullet. The impact should not create worse conditions for the player, and the asteroids should point away from the player.
- [ ] Implement tougher rocks that have a red tint. Players will need to shoot them repeatedly to remove the red color and eventually split them.
- [ ] ~~[Optional] Add Chuck Norris.~~ 

## Contributing

Contributions to Espaço are welcome! If you would like to contribute to the project, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch with a descriptive name:

```
python main.py
```

3. Make your desired changes to the codebase.

4. Test your changes to ensure they are functioning correctly.

5. Commit your changes with a meaningful commit message:

```
git commit -m "Add my feature"
```
6. Push your changes to your forked repository:

```

git push origin feature/my-feature

```

7. Open a pull request on the official Espaço repository, describing your changes and their purpose.

8. Wait for feedback and incorporate any suggested changes into your branch.

9. Once your changes are approved, they will be merged into the main project.

## License

Espaço is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as per the terms of the license.

## Special Thanks

Espaço extends its heartfelt thanks to the following individuals and resources:

- Lyle Rains and Ed Logg: Asteroids was conceived by Lyle Rains and programmed by Ed Logg, with collaborations from other Atari staff. Their pioneering work in the gaming industry has inspired countless developers, including Espaço.
- ChatGPT: The powerful language model developed by OpenAI that provided guidance and assistance during the creation of this project.
- GitHub Copilot: The AI-powered code completion tool that helped streamline the coding process and enhance productivity.
- The PyGame Community: The dedicated developers and contributors behind the PyGame library, whose efforts have made it possible to create engaging games in Python. Visit their website at [pygame.org](https://www.pygame.org/docs/) for more information.
- Python Docs: The official documentation for the Python programming language, which served as a valuable resource for understanding the language's features and capabilities. Explore the Python Docs at [python.org](https://www.python.org/doc/).

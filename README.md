# Automatic node startup

This is a Python script that starts up each Node-based project defined within a JSON file.
The script can easily be launched on startup, by making a shortcut of the run.bat file, and putting it in the windows startup folder.

## Supported Projects

Currently, there are 2 supported Node type projects, which can be hosted through this service.

- Traditional node project
- Vite react

Technically any project will work. Just add a script within package.json, which starts the project using "npm run dev" and set it as a react project within Projects.json
Changing the python script is also an easy option, to provide support for additional project types.

## Getting Started

### Prerequisites

- Python
- Node.js

### Installation and Setup

1. **Edit the Projects.json file**: Edit Projects.json with the correct information. This information is `path`, `type` and `port`
   - `path` has to go to the folder which your project is started from.
     - For `react` this is the root directory, which is with your `vite.config.ts`, `index.html` and src folder.
     - For `node` it is the location of your `index.js` file.
   - The `type` specifies the type of project. As mentioned earlier, this can be only `react` or `node`. Note that the `type` values are not case sensitive.
   - Lastly is the `port`. The Port is not gonna edit your project launch port. It only exists in the json objects, to keep track of 2 programs not using the same port. Head over to your project and change the actual port, to match the Project.json specified port. Having overlapping ports can cause issues.
     - For `react`, you can go into your `vite.config.ts` file and edit a few lines. An example can be found within `ViteReactExample.js`, in the `Port examples` folder.
     - For `node` projects, this can vary depending on how you create the project. An example can be found within `ApiNodeExample.js`, in the `Port examples` folder.
2. **Run the run.bat file**: Once all the information has been filled out, in the json object, run run.bat. This will launch all the node based projects, specified in the Projects.json file.
3. **Check the Logs folder**: If there are any errors, when running the program, an error log will be created.

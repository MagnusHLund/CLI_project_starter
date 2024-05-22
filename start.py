import json
import os
import subprocess
import datetime

def load_projects():
    """Load the project details from the JSON file."""
    # Open the JSON file in read mode
    with open('Projects.json', 'r') as json_file:
        # Parse the JSON file and return the result
        return json.load(json_file)

def check_ports(projects):
    """Check if multiple projects are using the same port."""
    try:
        # Create a list of all the ports used by the projects
        ports = [project['port'] for project in projects]
        # If the number of unique ports is less than the total number of ports,
        # it means that multiple projects are using the same port
        if len(ports) != len(set(ports)):
            raise ValueError("Multiple projects are using the same port")
    except Exception as e:
        # Log the error and re-raise the exception
        log_error(str(e))
        raise ValueError

def run_project(project, processes):
    """Run the appropriate command for the project based on its type."""
    try:
        # Define the path to the npm command
        npm_path = 'C:\\Program Files\\nodejs\\npm.cmd'
        # Check if the project path exists
        if not os.path.exists(project['path']):
            raise FileNotFoundError(f"Could not find project path {project['path']}")
        # Depending on the project type, run the appropriate command
        if project['type'].lower() == 'node':
            process = subprocess.Popen([npm_path, 'start'], cwd=project['path'], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        elif project['type'].lower() == 'react':
            process = subprocess.Popen([npm_path, 'run', 'dev'], cwd=project['path'], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        else:
            raise ValueError(f"Could not start {project['path']} as {project['type']} project")
        # Add the process to the list of processes
        processes.append(process)
    except Exception as e:
        # Log the error and stop all processes
        log_error(str(e))
        stop_processes(processes)

def stop_processes(processes):
    """Stop all processes."""
    # Terminate each process in the list of processes
    for process in processes:
        process.terminate()

def log_error(message):
    """Log the error message."""
    # Get the current date and time
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    # Open the log file in write mode
    with open(f"./Logs/{timestamp} log.txt", 'w') as log_file:
        # Write the error message to the log file
        log_file.write(message)
    # Print the error message
    print(f"An error occurred: {message}. Check the log file for details.")

def main():
    """Main function to load the projects and run each one."""
    # Load the projects from the JSON file
    projects = load_projects()
    # Create an empty list to store the processes
    processes = []
    # Check if multiple projects are using the same port
    check_ports(projects)
    # Run each project
    for project in projects:
        run_project(project, processes)
    # Keep the script running until the user presses enter
    input("Press enter to stop the script...")
    # Stop all child processes when the user presses enter
    stop_processes(processes)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
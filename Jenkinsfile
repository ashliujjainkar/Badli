pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ashliujjainkar/todo_list-flask-app' // Replace with your Docker Hub repo
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Starting to pull the repository..."
                git branch: 'main', url: 'https://github.com/ashliujjainkar/Badli.git'
                echo "Completed pulling the repository..."
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Reading version file"
                    def version = readFile('version.txt').trim()
                    echo "Version read from version.txt: ${version}"

                    echo "Starting to build docker image"
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                    echo "Completed building"
                }
            }
        }
    }
}

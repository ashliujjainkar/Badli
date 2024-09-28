pipeline {
    agent any

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
                    docker.build("ashliujjainkar/todo_list-flask-app:${version}")
                    echo "Completed building"
                }
            }
        }
    }
}

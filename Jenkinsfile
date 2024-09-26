pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ashliujjainkar/todo_list-flask-app' // Replace with your Docker Hub repo
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ashliujjainkar/Badli.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }
    }
}

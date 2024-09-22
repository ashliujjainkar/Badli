pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'https://index.docker.io/v1/' // If pushing to a registry
        DOCKER_IMAGE_NAME = 'ashliujjainkar/todo-flask-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/ashliujjainkar/Badli.git' // Replace with your Git repo URL
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Flask app Docker image
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Optionally, you can run tests here
                    echo 'Run tests here if needed'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // Run the app in Docker
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean up workspace after each build
        }
    }
}

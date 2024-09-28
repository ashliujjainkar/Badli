pipeline {
    agent any

    environment {
        IMAGE_VERSION = ''
    }

    stages {
        stage('Setup Workspace') {
            steps {
                script {
                    // Create a unique temporary directory for the build
                    def tempWorkspace = "${env.WORKSPACE}/build-${env.BUILD_ID}"
                    dir(tempWorkspace) {
                        // Use this directory as the workspace for all subsequent steps
                        env.WORKSPACE = tempWorkspace
                    }
                }
            }
        }
        stage('Clone Repository') {
            steps {
                dir(env.WORKSPACE) {
                    echo 'Starting to pull the repository...'
                    git branch: 'main', url: 'https://github.com/ashliujjainkar/Badli.git'
                    echo 'Completed pulling the repository...'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir(env.WORKSPACE) {
                    script {
                        echo 'Reading version file'
                        IMAGE_VERSION = readFile('version.txt').trim()
                        echo "Version read from version.txt: ${IMAGE_VERSION}"

                        echo 'Starting to build docker image'
                        docker.build("ashliujjainkar/todo_list-flask-app:${IMAGE_VERSION}")
                        echo 'Completed building'
                    }
                }
            }
        }

        // stage('Run Docker Compose') {
        //     steps {
        //         script {
        //             echo "starting docker compose"
        //             sh "IMAGE_VERSION=${IMAGE_VERSION} docker-compose up -d --build"
        //             echo "completed docker compose"
        //         }
        //     }
        // }

        // stage('Test /version API') {
        //     steps {
        //         script {
        //             sleep 10

    //             def response = sh(script: "curl -o /dev/null -s -w '%{http_code}' http://localhost:5000/version", returnStdout: true).trim()
    //             if (response != '200') {
    //                 error "Version API returned status ${response}"
    //             }
    //         }
    //     }
    // }
    }
}

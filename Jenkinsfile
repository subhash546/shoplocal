pipeline {
    agent any

    environment {
        IMAGE_NAME = "subhashrowtu/shoplocal-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Version') {
            steps {
                script {
                    if (env.BRANCH_NAME == "main") {
                        VERSION = "prod-${BUILD_NUMBER}"
                    } else if (env.BRANCH_NAME == "stage") {
                        VERSION = "staging-${BUILD_NUMBER}"
                    } else {
                        VERSION = "dev-${BUILD_NUMBER}"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$VERSION ."
            }
        }

     stage('Push Image to DockerHub') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'USER',
            passwordVariable: 'PASS'
        )]) {
            sh """
            docker tag $IMAGE_NAME:$VERSION $IMAGE_NAME:latest
            docker push $IMAGE_NAME:latest
            """
        }
    }
}

        stage('Info') {
            steps {
                echo "Built Image: ${IMAGE_NAME}:${VERSION}"
            }
        }
    }
}
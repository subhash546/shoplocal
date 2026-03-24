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
            def branch = env.GIT_BRANCH

            // get commit count of current branch
            def commitCount = sh(
                script: "git rev-list --count HEAD",
                returnStdout: true
            ).trim()

            echo "Branch: ${branch}"
            echo "Commit Count: ${commitCount}"

            if (branch.contains("main")) {
                VERSION = "prod-${commitCount}"
            } else if (branch.contains("stage")) {
                VERSION = "staging-${commitCount}"
            } else {
                VERSION = "dev-${commitCount}"
            }

            echo "Final Version: ${VERSION}"
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
        script {
            withCredentials([usernamePassword(
                credentialsId: 'subhash-creds',
                usernameVariable: 'USER',
                passwordVariable: 'PASS'
            )]) {
                sh """
                echo "Logging into DockerHub..."
                echo \$PASS | docker login -u \$USER --password-stdin

                echo "Pushing version..."
                docker push $IMAGE_NAME:$VERSION

                echo "Tagging latest..."
                docker tag $IMAGE_NAME:$VERSION $IMAGE_NAME:latest

                echo "Pushing latest..."
                docker push $IMAGE_NAME:latest
                """
            }
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
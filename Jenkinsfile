pipeline {
  environment {
    registry = "YOUR_REGISTRY"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/almoggo/rpi-face-detection.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build("$registry:$BUILD_NUMBER") 
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
    stage('template the kubernetes creation yml ') {
      steps{
        ansiblePlaybook(
          playbook: 'template.yml',
          extraVars: [
              buildId: '$BUILD_NUMBER',
              jobName: '$JOB_NAME'
          ])
      }
    }
    stage('deploy the application on kubernetes cluster') {
        steps{
            sh "kubectl apply -f /var/lib/jenkins/workspace/$JOB_NAME/kuberenetesResources/full-deployment.yml"
        }
    }
  }
}

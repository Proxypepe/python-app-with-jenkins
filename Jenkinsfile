def imageName = 'proxypepe/demo'

node('master'){
  stage('Checkout') {
    steps {
      git branch: 'develop',
        credentialsId: 'github-ssh',
        url: 'git@github.com:.git'
    }
  }
    // stage('Unit Tests'){
  //   def imageTest = docker.build("${imageName}-test", 
  //   "-f Dockerfile.test .")
  //   imageTest.inside{
  //     sh 'python test_main.py'
  //   }
  //   // sh "docker run --rm -v $PWD/reports:/app/reports ${imageName}-test"
  //   // junit "$PWD/reports/*.xml"
  // }
  def imageTest= docker.build("${imageName}-test", "-f Dockerfile.test .")
  stage('Pre-integration Tests'){
    parallel(
      'Quality Tests': {
          imageTest.inside{
            sh 'pylint .'
        }
      },
       'Unit Tests': {
          imageTest.inside{
            sh 'pytest'
          }
        },
      'Security Tests': {
        imageTest.inside(){
          sh 'safety check -r main.py'
        }
      }
    )
  }
}

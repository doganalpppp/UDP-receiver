pwd=$PWD
mkdir build 
cd build
conan install $pwd
conan build $pwd
build_result=$?

conan source $pwd 

exit ${build_result}
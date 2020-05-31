echo OS_VERS=$(grep -oP '(?<=^PRETTY_NAME=).+' /etc/os-release | tr -d '"')
echo PELICAN_VERS=$(pelican --version)
echo BASH_VERS=${BASH_VERSION}
echo FFMPEG_VERS=$(ffmpeg -version | sed -n "s/ffmpeg version \([-0-9.]*\).*/\1/p;")
echo IMAGEMAGICK_VERS=$(identify -version | sed -n "s/Version: ImageMagick \([-0-9.]*\).*/\1/p;")
echo PYTHON_VERS=$(python --version | sed -n "s/Python \([-0-9.]*\).*/\1/p;")
echo YOUTUBE-DL_VERS=$(youtube-dl --version)
echo AUDACITY_VERS=$(audacity --version | sed -n "s/Audacity v \(v[-0-9.]*\).*/\1/p;")
echo GIT_VERS=$(git --version | sed -n "s/git version \([-0-9.]*\).*/\1/p;")
echo DAVINCI_VERS=$(apt show davinci-resolve | sed -n "s/Version: \([-0-9.]*\).*/\1/p;")


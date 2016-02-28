from distutils.core import setup
setup(
  name = 'restplayer',
  packages = ['restplayer'],
  version = '0.1',
  description = 'A Seamless Remote layer',
  author = 'Cristiano Werner Araujo',
  author_email = 'cristianowerneraraujo@gmail.com',
  url = 'https://github.com/cristianowa/restplayer',
  download_url = 'https://github.com/cristianowa/restplayer/archive/0.1.tar.gz', 
  keywords = ['remote player', 'mp3', 'music', 'vlc'],
  classifiers = ["Development Status :: 3 - Alpha",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "License :: OSI Approved :: BSD License",],
  scripts = ["restplayer/restplayer.py"]
)

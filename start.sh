if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Aneebrahman/LUCIFER-FILE-SHARING-BOT.git /LUCIFER FILE SHARE BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LUCIFER FILE SHARE BOT
fi
cd /LUCIFER FILE SHARE BOT
pip3 install -U -r requirements.txt
echo "𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜....🍁"
python3 bot.py

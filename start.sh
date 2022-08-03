if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/salvin308/Adv-AutoFilter-Bot.git /Adv-AutoFilter-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Adv-AutoFilter-Bot
fi
cd /Adv-AutoFilter-Bot
pip3 install -U -r requirements.txt
echo "Starting AutoFilterBot....🔥"
python3 main.py

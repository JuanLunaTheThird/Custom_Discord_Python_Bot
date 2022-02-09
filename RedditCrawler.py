import praw
from requests import Session
from datetime import datetime

reddit = praw.Reddit(
    client_id="t_zrq4cg5RGfrg",
    client_secret="D91fzHZ-iPGtL1xPWf_DSkAr99O5jA",
    user_agent="Subreddit keyword searcher by /u/Neoreaperblade",
)


def get_monitor_sales():
    sales = []
    for submission in reddit.subreddit('buildapcsales').new():
        if 'Monitor' in submission.title:
            time = datetime.fromtimestamp(submission.created_utc)
            time = time.strftime('%Y/%m/%d %I:%M:%p')
            link_for_post = submission.permalink
            tuple = (submission.title, submission.url, time, link_for_post)
            sales.append(tuple)

    return sales


def write_to_file(sales):
    txt = open("sales.txt", "w")
    for s in sales:
        string = "Submission Name: " + str(s[0]) + '\n' + " url: " + s[1] + '\n' + "  submitted: " + str(s[2]) + '\n'
        string += "     Reddit Link:  " + 'https://www.reddit.com' + s[3] + '\n'
        txt.write(string)
        txt.write('\n')
    txt.close()


if __name__ == "__main__":
    sales = get_monitor_sales()
    write_to_file(sales)

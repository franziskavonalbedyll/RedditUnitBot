import praw
import passwords as pwd
import conversion as con

def main():
    reddit = praw.Reddit(
        client_id=pwd.reddit["client_id"],
        client_secret=pwd.reddit["client_secret"],
        user_agent="RedditUnitBot (by u/RedditUnitBot)",
    )

    print(con.milestoKM(1))
    print(con.kmtoMiles(1))
    print(con.inchtoCm(1))
    print(con.cmtoInch(1))
    print(con.foottoCM(1))
    print(con.cmtoFoot(1))
    print(con.foottoMeter(1))
    print(con.metertoFoot(1))
    print(con.poundstoKg(1))
    print(con.kilogrammtoPounds(1))
    print(con.celsiustoFahrenheit(1))
    print(con.fahrenheittoCelsius(1))



if __name__ == "__main__":
    main()
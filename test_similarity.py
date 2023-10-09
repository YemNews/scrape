from similarity import assign_interest
import csv


generative_ai_recurring = [{"title":"Everyone wants to make AI chips, UK antitrust hawks eye cloud ... - SiliconANGLE News","interests":["new llms in gen ai","new startups"]},
                           {"title":"Bot AI Being General Artificial Intelligence Lives - Digital Journal","interests":["new llms in gen ai","new regulations"]},
                           {"title":"5 questions for Google's Yasmin Green - POLITICO - POLITICO","interests":["new llms in gen ai","new regulations"]},
                           {"title":"Food Services Employment Returns to Pre-Pandemic Level With ... - PYMNTS.com","interests":["new llms in gen ai","new startups"]},
                           {"title":"AI Is Nowhere Near Being Able to Remake ‘Breakfast at Tiffany’s’ With a Different Actor – Yet | Video - Yahoo Entertainment","interests":["new llms in gen ai","new regulations"]},
                           {"title":"An AI for an AI. As Amazon invests up to $4 billion in… | by Onuche ... - Medium","interests":["new llms in gen ai","new startups","new regulations"]},
                           {"title":"Graphcore is struggling — what's gone wrong for the once 'NVIDIA ... - Sifted","interests":["new llms in gen ai","new startups"]},{"title":"Steer Clear of These Cash-Strapped Tech Stocks - Brownstone Research","interests":["new llms in gen ai","new startups","new regulations"]},
                           {"title":"An AI for an AI. As Amazon invests up to $4 billion in… | by Onuche ... - Medium","interests":["new llms in gen ai","new startups","new regulations"]},
                           {"title":"The Ozone Hole Above Antarctica Has Grown To Three Times the ... - Slashdot","interests":["new llms in gen ai","new regulations"]},
                           {"title":"Visa to invest $100 mn in generative AI companies","interests":["new llms in gen ai","new startups"]},
                           {"title":"Everyone wants to make AI chips, UK antitrust hawks eye cloud providers, and MGM rebuffs ransom demand","interests":["new llms in gen ai","new startups"]},
                           {"title":"People Are Eagerly Consulting Generative AI ChatGPT For Mental Health Advice, Stressing Out AI Ethics And AI Law","interests":["new llms in gen ai","new regulations"]},
                           {"title":"Generative AI biggest game-changer in education since '90s internet boom, UAE experts say","interests":["new llms in gen ai","new regulations"]},
                           {"title":"Generative AI matches accuracy, quality of radiologist reports in study","interests":["new llms in gen ai","new regulations"]},
                           {"title":"Google Execs Foresee Generative AI as Potential $210 Billion Boost to Canada’s Economy","interests":["new llms in gen ai","new startups"]},
                           {"title":"Biggest AI Systems Poised for Stricter Set of EU Rules - Yahoo Finance","interests":["new startups","new regulations"]},
                           {"title":"Generating less momentum? Generative AI deal count dips in Q3 - PitchBook News & Analysis","interests":["new startups","new regulations"]},
                           {"title":"ByteDance Stock Is Very Cheap—for Good Reason - The Information","interests":["new startups","new regulations"]},
                           {"title":"Education, ecommerce, EVs: test your business creativity with ... - YourStory","interests":["new startups","new regulations"]},
                           {"title":"Form N-CSR Ark Venture Fund For: Jul 31 - StreetInsider.com","interests":["new startups","new regulations"]},
                           {"title":"Australia’s Telecommunications Industry Following Global Peers on Generative AI","interests":["new startups","new regulations"]}]


printing_and_packaging_recurring = [{"title":"3D Printing News Briefs, October 7, 2023: 3D Printed Submarine Parts, Model Sharing, & More - 3DPrint.com","interests":["Techs","General updates"]},
                                    {"title":"Global Printed, Flexible and Hybrid Electronics Markets, 2018-2023 ... - PharmiWeb.com","interests":["Techs","Trends"]},
                                    {"title":"No Experience Sales Trainee / Business Development Trainee Jobs – Uneeco Uganda Ltd","interests":["Techs","Trends"]},
                                    {"title":"A Tribute to West Bengal: Asian Paints celebrates the state’s creativity, traditions, and spirit of Durga Pujo!","interests":["Techs","Trends"]},
                                    {"title":"Online Shopping Boom Spurs Demand for Shaped Corrugated Packaging, Despite Challenges of Moisture Sensitivity and Limited Barrier Properties","interests":["Techs","Trends"]},
                                    {"title":"Paper Cushioning Systems: Affordable and Effective Protection for Delicate Cargo in Logistics and Shipping","interests":["Techs","Trends"]},
                                    {"title":"BASF Celebrates 25 Years of ecoflex® Biopolymer, Pioneering Sustainability in Plastics","interests":["Techs","General updates","Trends"]},
                                    {"title":"EBRD Extends €4 Million Loan to KEP Trust to Boost MSMEs and Female Entrepreneurs in Kosovo","interests":["Techs","General updates","Trends"]}]

localnews_cali_recurring = [{"title":"Disneyland Plans Expansion; Big Skate Babies Hatch: Saturday Smiles - Patch","interests":["General Updates","Local Entertainment","Community Events"]},
                            {"title":"Honolulu News","interests":["General Updates","Local Entertainment","Community Events"]},
                            {"title":"Milwaukee News","interests":["General Updates","Community Events"]},
                            {"title":"Clark County News","interests":["General Updates","Local Entertainment","Community Events"]},
                            {"title":"Pennsylvania News","interests":["General Updates","Local Entertainment"]},
                            {"title":"Resort Lodge in Walker Destroyed by Early Morning Fire - WJON News","interests":["Local Entertainment","Community Events"]},
                            {"title":"You Won't Believe What Someone Brought Into The MN Airport - US 103.3","interests":["Local Entertainment","Community Events"]},
                            {"title":"Banned Books Week Ends At Riverside County Libraries: Let Freedom Read","interests":["Local Entertainment","Community Events"]},
                            {"title":"Walking and Rolling","interests":["Local Entertainment","Community Events"]},
                            {"title":"Open Mic at the Cinema continues to thrive","interests":["Local Entertainment","Community Events"]}]


def collate_assign_interests_tocsv(name:str, topic:list):
    with open(f'{name}.csv','w+') as csvfile:
        csvwriter = csv.writer(csvfile)
        fields = ['title','overlapping_interests','chosen_interest']
        csvwriter.writerow(fields)
        for article in topic:
            title = article['title']
            interests = article['interests']
            chosen_interest = assign_interest(title, interests)
            csvwriter.writerow([title, interests, interests[chosen_interest]])
            print(f'TITLE: {title}\nOVERLAPPING INTERESTS: {interests}\nCHOSEN INTEREST: {interests[chosen_interest]}\n\n')
        
collate_assign_interests_tocsv('genai', generative_ai_recurring)
collate_assign_interests_tocsv('printingpackaging', printing_and_packaging_recurring)
collate_assign_interests_tocsv('localnewscali', localnews_cali_recurring)
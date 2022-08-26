from os import remove
from sys import argv, exit
from requests import Session
from bs4 import BeautifulSoup

def main():
    args = argv[1:]
    if len(args) > 0:

        for url in args:
            toc = str()
            
            session = Session()
            
            try:
                response = session.get(url.strip())

                file_name = url.strip('/').split('/').pop() + '.md'

                html_soup = BeautifulSoup(response.text, 'html.parser')

                tags = html_soup.find_all(["h2", "h3"])

                for tag in tags:
                    line = f"- [{tag.text}](#{tag['id']})\n"
                    if tag.name == 'h3':
                        line = '    ' + line
                    toc += line
            except:
                exit("OOPS! THAT DIDN'T GO ACCORDING TO PLAN.")

            try:
                remove(file_name)
            except OSError:
                pass

            with open(file_name, 'a', encoding='utf-8') as toc_file:
                toc_file.write(toc)
    else:
        exit("NO ARGUMENT PASSED.")

if __name__ == "__main__":
    main()
from anlib.helpers import get_article, handle_article

import argparse


def main():
    parser = argparse.ArgumentParser(description='Process search term query.')
    parser.add_argument('query', metavar='query',  help='the query to search \
                        on the Anarchist library website')
    parser.add_argument('-e', '--ext', default='.html', choices=['.html',
                        '.pdf'], help='specify the file extension')
    parser.add_argument('-m', '--method', default='launch', choices=['launch',
                        'download'], help='choose whether to launch the file \
                        automatically or download it locally')

    parsed = parser.parse_args()

    if get_article(parsed.query) is None:
        print('No results found, try searching for something else.')
        return

    return handle_article(get_article(parsed.query), parsed.ext, parsed.method)


if __name__ == '__main__':
    main()

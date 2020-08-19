import sys
import markdown2

PRE_TEMPLATE = 'PRE.partial.html'
POST_TEMPLATE = 'POST.partial.html'

if __name__ == '__main__':
    if len(sys.argv) == 3:
        in_name = sys.argv[1]
        out_name = sys.argv[2]

    # If people actually make blog posts
    # I'll make this tool better...
    html = ''
    with open(PRE_TEMPLATE) as f:
        html += f.read()

    markdown_html = markdown2.markdown_path(in_name)
    html += markdown_html

    with open(POST_TEMPLATE) as f:
        html += f.read()

    with open(out_name, "w") as f:
        f.write(html)

    print("HTML can now be found at ", out_name)

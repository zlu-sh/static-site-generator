from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text.split(delimiter)

            if len(node_text) % 2 == 0:
                raise ValueError("Invalid markdown, unpaired delimiters")
            for i, text in enumerate(node_text):
                if text == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(text, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(text, text_type))

    return new_nodes

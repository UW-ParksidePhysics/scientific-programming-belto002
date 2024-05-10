import matplotlib.pyplot as plt


def annotate_plot(annotations_dict):
    """
    Annotates a plot with the specified annotations.

    Parameters:
        annotations_dict (dict): A dictionary where keys are the labels to be annotated
            and values are dictionaries containing annotation information.
            Each annotation dictionary should have the following keys:
            - 'position': tuple, the (x, y) coordinates for the position of the textbox
            - 'alignment': tuple or str, optional, the horizontal and vertical alignment
                values for the text function. Default is ('left', 'bottom').
            - 'fontsize': int, optional, the font size in points. Default is 10.

    Returns:
        None

        __author__ = Jackson
    """
    for label, annotation_info in annotations_dict.items():
        position = annotation_info['position']
        alignment = annotation_info.get('alignment', ('left', 'bottom'))
        fontsize = annotation_info.get('fontsize', 10)
        plt.text(position[0], position[1], label, fontsize=fontsize, horizontalalignment=alignment[0],
                 verticalalignment=alignment[1])


if __name__ == "__main__":
    # Test the module
    annotations = {
        "Created by Jackson Beltoya": {
            'position': (0.02, 0.02),
            'alignment': ('left', 'bottom'),
            'fontsize': 8
        }
    }
    annotate_plot(annotations)
    plt.show()

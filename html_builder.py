"""
Purposely HARDCODED.
Author - Amr Mualla
Project - My Little Web Page.
The program below builds a very simple web page, based on a users desires, with either
user input or redirected input. The program also can be used in two modes, a wizard mode
and a website mode. In the wizard mode, the user inputs all the information for their webpage.
In website mode, the user puts a file in the command line arguments, and the program creates
the webpage based on the details within the textfile. In website mode, multiple text files
can be placed in the command line arguments and the program will create each webpage and link
them together aswell. 
"""

from dataclasses import dataclass
import turtle
import fileinput
from turtle import *
import string
from typing import List
import sys

@dataclass
class webpage:
    style: str
    title: str
    paragraphamt: List['paragraph']

@dataclass
class paragraph:
    title: str
    text: str
    images: List[str]

COLORS = ['peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen', 'lawngreen',
 'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen', 'chocolate', 'yellowgreen',
 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat', 'mediumvioletred', 'bisque', 'lightgreen', 'cyan',
 'hotpink', 'gray', 'indianred', 'antiquewhite', 'royalblue', 'yellow', 'indigo', 'lightcoral', 'darkslategrey',
 'sienna', 'lightslategray', 'mediumblue', 'red', 'khaki', 'darkviolet', 'mediumorchid', 'darkblue', 'lightskyblue',
 'turquoise', 'lightyellow', 'grey', 'whitesmoke', 'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise', 'coral',
 'forestgreen', 'gainsboro', 'darkorange', 'cornflowerblue', 'lightsteelblue', 'plum', 'lavender', 'palegreen', 'darkred',
 'dimgray', 'floralwhite', 'orangered', 'oldlace', 'darksalmon', 'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver',
 'tomato', 'darkkhaki', 'slategray', 'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson', 'mistyrose', 'lime', 'saddlebrown',
 'blanchedalmond', 'black', 'snow', 'seashell', 'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod', 'palevioletred', 'fuchsia',
 'teal', 'lightpink', 'darkgrey', 'mediumspringgreen', 'aquamarine', 'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood',
 'rosybrown', 'springgreen', 'purple', 'olivedrab', 'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine', 'navy',
 'salmon', 'rebeccapurple', 'darkmagenta', 'limegreen', 'deepskyblue', 'pink', 'mediumpurple', 'skyblue', 'aqua', 'blue',
 'slategrey', 'darkslateblue', 'honeydew', 'darkseagreen', 'paleturquoise', 'brown', 'thistle', 'lemonchiffon', 'peru',
 'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow', 'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey',
 'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite', 'dodgerblue', 'greenyellow', 'dimgrey', 'darkorchid']

def hexadecimals(value):
    """
    This function takes the user input/redirect input value for their choice of a color
    and returns True or False, based on whether or not the color is a legal format. In other words,
    it returns True if its a correct hexidecimal or if the color is in list COLORS.
    :param value: The users input value for a color.
    :return: True or False, based on whether the users input value is legal.
    """
    hexidecimal = ['0', '1', '2', '3', '4', '5', '6', '8', '9', 'a', 'b',
                   'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
    colorstr = str(value)
    loweredcolor = colorstr.lower()
    if loweredcolor in COLORS:
        Answer = True
    elif value[0] == '#' and len(value) == 7:
        for val in value[1:]:
            if val in hexidecimal:
                Answer = True
            elif val not in hexidecimal:
                Answer = False
                break
    else:
        Answer = False
    return Answer




def validfont(value):
    """
    This function takes the user input/redirected input value for their choice of a font
    and returns True or False, based on whether or not the choice is valid. Choices that are
    valid are numbers 1-6, to represent the 6 types of fonts given to choose from.
    :param value: The users input value for a font choice.
    :return: True or False, based on whether or not the users input value is valid.
    """
    validnumbers = ['1', '2', '3', '4', '5', '6']
    if value in validnumbers:
        Answer = True
    else:
        Answer = False

    return Answer




def fontwindow():
    """
    This function simply opens the turtle window displaying all the fonts.
    :return: Does not return anything.
    """
    window = turtle.Screen()
    window.setup(width=300, height=280)
    turtle.hideturtle()
    pen1 = Pen()
    pen1.speed(0)
    pen1.color('black', 'green')
    pen1.hideturtle()
    pen1.up()
    pen1.goto(-130, 100)
    pen1.down()
    pen1.write("Arial", False, 'left', font=('Arial', 16, 'normal'))
    pen1.up()
    pen1.goto(-130, 75)
    pen1.down()
    pen1.write("Comic Sans MS", False, 'left', font=('Comic Sans MS', 16, 'normal'))
    pen1.up()
    pen1.goto(-130, 50)
    pen1.down()
    pen1.write('Lucida Grande', move=False, align="left", font=("Lucida Grande", 16, "normal"))
    pen1.up()
    pen1.goto(-130, 25)
    pen1.down()
    pen1.write('Tahoma', move=False, align="left", font=("Tahoma", 16, "normal"))
    pen1.up()
    pen1.goto(-130, 0)
    pen1.down()
    pen1.write('Verdana', move=False, align="left", font=("Verdana", 16, "normal"))
    pen1.up()
    pen1.goto(-130, -25)
    pen1.down()
    pen1.write('Helvetica', move=False, align="left", font=("Helvetica", 16, "normal"))
    pen1.up()
    pen1.goto(-130, -50)
    pen1.down()
    pen1.write('Times New Roman', move=False, align="left", font=("Times New Roman", 16, "normal"))
    turtle.exitonclick()




def colorandfont(Website):
    """
    This function takes a parameter Website, which is defined in the Wizardmode() or Websitemode()
    as an empty webpage dataclass. This function asks the user for all their input values for the colors
    and fonts which will be used in both wizardmode and websitemode. Then this function opens the style template
    and saves it as a string, and replaces the style variables with the users input. Lastly, the function saves
    the style string to the Website structure.
    :param Website:
    :return: Returns the string of the style template to be used in the Websitemode function.
    """
    print('Background Color')
    backgroundcolor = input("Choose the name of a color, or in format '#XXXXXX':")
    validbackgroundcolor = hexadecimals(backgroundcolor)
    while validbackgroundcolor == False:
        print('Illegal Format')
        backgroundcolor = input("Choose the color name or #XXXXXX")
        validbackgroundcolor = hexadecimals(backgroundcolor)
    print('You will now choose a font.')
    fontdisplay = input("Do you want to see what the fonts look like? [yes]")
    if fontdisplay == 'yes' or fontdisplay == "":
        fontwindow()
    else:
        pass
    print('Choose a font by its number.')
    print('0: Arial, size 16')
    print('1: Comic Sans MS, size 16')
    print('2: Lucida Grande, size 16')
    print('3: Tahoma, size 16')
    print('4: Verdana, size 16')
    print('5: Helvetica, size 16')
    print('6: Times New Roman, size 16')
    fontchosen1 = input("")
    validfontchosen = validfont(fontchosen1)
    while validfontchosen == False:
        print('Not a valid choice')
        fontchosen1 = input('Choose again: ')
        validfontchosen = validfont(fontchosen1)
    print('Paragraph Text Color')
    fontcolor = input("Choose the name of the color, or in format '#XXXXXX': ")
    validfontcolor = hexadecimals(fontcolor)
    while validfontcolor == False:
        print('Illegal Format')
        fontcolor = input("Choose the color name or #XXXXXX")
        validfontcolor = hexadecimals(fontcolor)
    print('Heading Color')
    headingcolor = input("Choose the name of the color, or in format '#XXXXXX: ")
    validheadingcolor = hexadecimals(headingcolor)
    while validheadingcolor == False:
        print('Illegal Format')
        headingcolor = input("Choose the color name or #XXXXXX")
        validheadingcolor = hexadecimals(headingcolor)

    if fontchosen1 == '0':
        realfont = 'Arial'
    elif fontchosen1 == '1':
        realfont = "Comic Sans MS"
    elif fontchosen1 == '2':
        realfont = "Lucida Grande"
    elif fontchosen1 == '3':
        realfont = "Tahoma"
    elif fontchosen1 == '4':
        realfont = "Verdana"
    elif fontchosen1 == '5':
        realfont = "Helvetica"
    else:
        realfont = "Times New Roman"

    with open('style_template.txt', 'r') as file:
        data = file.read().replace('', '')
        data1 = data.replace('@BACKCOLOR', backgroundcolor, 1)
        data2 = data1.replace('@HEADCOLOR', headingcolor, 2)
        data3 = data2.replace('@FONTSTYLE', realfont, 3)
        finaldata = data3.replace('@FONTCOLOR', fontcolor, 1)
        Website.style = finaldata
        return finaldata




def buildwebpage(Website, htmlargument, link):
    """
    This function takes the datastructures that have been made, iterates over the list of paragraphs in the datastructure
    and creates a string of html code representing all paragraphs. The function then checks if it is wizard mode or
    website mode and aligns html writing and datastructure components and then saves it all to a string. Lastly, the program
    outputs the html code. If the program is in wizard mode it will write the html code to a html file titled index.html,if
    it is website mode it will write the html code to a html file titled with the value of the command line argument.
    :param Website: A datastructure of the webpage that is filled with the webpage information.
    :param htmlargument: a string of the command line argument, with .txt replaced with .html (if in website mode)
    :param link: a string of html code linking the webpages together (if in website mode)
    :return: Does not return anything.
    """
    websitestr = ""
    for paragraph in Website.paragraphamt:
        website1 = ("<h2>" + paragraph.title + "\n"
                    "</h2>\n" +
                    "<p>" + paragraph.text + "\n"
                    "</p>\n")
        for images in paragraph.images:
            website1 = website1 +  ("<img src=" + images + ' class="center">\n')
        websitestr = websitestr + website1

    if len(sys.argv) == 1:
        completewebsite = ("<!DOCTYPE html>\n"
                           "<html>\n" +
                           "<head>\n" +
                           "<title>" + Website.title + "\n"
                           "</title>" + Website.style + "\n"
                           "</head>\n" +
                           "<body>\n" +
                           "<h1>" + Website.title + "\n"
                           "</h1>\n" +
                           "<hr/>\n" +
                           websitestr + "\n"
                           "</body>\n" +
                           "</html>\n")
    elif len(sys.argv) > 1:
        completewebsite = ("<!DOCTYPE html>\n"
                           "<html>\n" +
                           "<head>\n" +
                           "<title>" + Website.title + "\n"
                           "</title>" + Website.style + "\n"
                           "</head>\n" +
                           "<body>\n" +
                           "<h1>" + Website.title + "\n"
                           "</h1>\n" +
                           "<hr/>\n" +
                           "<p align='center'>" + link + "\n" +
                           "</p>\n" +
                           websitestr + "\n"
                           "</body>\n" +
                           "</html>\n")

    if len(sys.argv) == 1:
        my_file = open("indexx.html", "w+")
        my_file.write(completewebsite)
    elif len(sys.argv) > 1:
        my_file = open(htmlargument, "w+")
        my_file.write(completewebsite)




def title(Website):
    """
    This function simply asks the user for the title of their website, and makes that the title
    in the webpage dataclass named Website. (Used in wizard mode only)
    :param Website: A webpage datastructure.
    :return: Does not return anything.
    """
    websitetitle = input("What is the title of your website?")
    Website.title = websitetitle




def textquestions(Website):
    """
    This function asks the user for all the content of the website, including paragraph titles, paragraph text,
    and images. This function updates the webpage dataclass known as Website with relevant information (userinput)
    (This function is only used in Websitemode).
    :param Website: A webpage datastructure.
    :return: A filled webpage dataclass stored in variable Website.
    """
    paratitle = input("What is the title of your paragraph: ")
    thepara = paragraph(title='', text='', images=[])
    thepara.title = paratitle
    content = input('Content of your paragraph (single line)')
    thepara.text = content
    imagechoice = input("Do you want to add images? [yes]")
    if imagechoice == 'yes' or imagechoice == "":
        imagefile = input('Image file name:')
        thepara.images.append(imagefile)
        anotherimage = input("Do you want to add another image? [yes]")
    else:
        anotherimage = 'no'
    if anotherimage == 'yes' or anotherimage == "":
        imagefile2 = input('Image file name:')
        thepara.images.append(imagefile2)
    while anotherimage == 'yes' or anotherimage == "":
        anotherimage = input("Do you want to add another image? [yes]")
        if anotherimage == 'yes' or anotherimage == "":
            imagefile3 = input('Image file name:')
            thepara.images.append(imagefile3)
    Website.paragraphamt.append(thepara)
    anotherparagraph = input('Do you want to add another paragraph to your website? [yes]')
    if anotherparagraph == 'yes' or anotherparagraph == "":
        textquestions(Website)
    else:
        return Website




def converttostr(lst, seperator):
   """
   This function combines all strings in a list into a single string. It is used mostly in Websitemodecode() to
   convert lists into strings.
   :param input_seq: a list of strings
   :param seperator: what you wish to seperate the strings by
   :return: the converted string
   """
   final = seperator.join(lst)
   return final




def Websitemodecode(Website, arg):
    """
    This function is used in (website mode) and takes the command line argument, opens the text file, parses the content inside
    and builds the webpage datastructure.
    :param Website: A webpage datastructure
    :param arg: The command line argument.
    :return:
    """
    OpeningText = open(arg, 'r',errors='ignore')
    lstoftext = OpeningText.read()
    SeperatebyPara = lstoftext.split('!new_paragraph')
    OpeningText.close()
    Website.title = SeperatebyPara[0]
    titlevalue = SeperatebyPara[0]
    SeperatebyPara.remove(titlevalue)
    for item in SeperatebyPara:
        thepara = paragraph(title='', text='', images=[])
        Seperatetitles = item.split('!title')
        StringForm = converttostr(Seperatetitles, '')
        Addingtitle = StringForm.split('\n',2)
        thepara.title = Addingtitle[1]
        Addingtitle.remove(thepara.title)
        Reverseback = converttostr(Addingtitle, '')
        FinalSeperation = Reverseback.split('!image')
        thepara.text = FinalSeperation[0]
        FinalSeperation.remove(thepara.text)
        for image in FinalSeperation:
            thepara.images.append(image)
        Website.paragraphamt.append(thepara)




def linkingthesites():
    """
    This function simply returns a string of html links that will be placed in the html string used in
    buildwebpage().
    :return: string of html links
    """
    link = ''
    arguments = (sys.argv)
    arguments1 = arguments[1:]
    for arg in arguments1:
        Website = webpage(style='', title='', paragraphamt=[])
        htmlargument = arg.replace('txt', 'html')
        Websitemodecode(Website, arg)
        link = link + "<a href=" + '"' + htmlargument + '"' + ">" + Website.title + "</a>---"
        link = link.replace('\n', '')
    return link




def Wizardmode():
    """
    This function combines the necessary functions to create wizard mode. It creates a empty webpage datastructure,
    and as it goes through the function the datastructure gets filled up and when it reaches buildwebpage() it is
    built into an html file. The file is saved as 'indexx.html'.
    :return: Does not return anything.
    """
    Website = webpage(style='', title='', paragraphamt=[])
    arg = ''
    link = ''
    title(Website)
    colorandfont(Website)
    textquestions(Website)
    buildwebpage(Website, arg, link)
    print('Your website has been saved as indexx.html')




def Websitemode():
    """
    This function combines the necessary functions to create website mode. It creates an empty webpage datastructure,
    and as it goes through the function the datastructure gets filled up and when it reaches buildwebpage() it is built
    into into html file(s), with titles based on the text files in which the content originated.
    :return: This function does not return anything.
    """
    Website = webpage(style='', title='', paragraphamt=[])
    arguments = (sys.argv)
    arguments1 = arguments[1:]
    style = colorandfont(Website)
    link = linkingthesites()
    for arg in arguments1:
        Website = webpage(style='', title='', paragraphamt=[])
        Website.style = style
        htmlargument = arg.replace('txt', 'html')
        Websitemodecode(Website, arg)
        buildwebpage(Website, htmlargument, link)

def main():
    """
    This function decides whether to use wizard mode or website mode based on the length of the command line arguments.
    :return: This function does not return anything.
    """
    if len(sys.argv) == 1:
        Wizardmode()
    elif len(sys.argv) > 1:
        Websitemode()

main()
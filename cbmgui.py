#!/usr/bin/python3
import PySimpleGUI as sg
import glob
import ntpath
import subprocess

LOCATION_OF_YOUR_SCRIPTS = ''

# Execute the command.  Will not see the output from the command until it completes.
def execute_command_blocking(command, *args):
    expanded_args = []
    for a in args:
        expanded_args.append(a)
        # expanded_args += a
    try:
        sp = subprocess.Popen('./dir.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        out = ''
    return out


def Launcher2():
    sg.ChangeLookAndFeel('DarkBlue')
    form = sg.FlexForm('Open CBM GUI')

    filelist = glob.glob(LOCATION_OF_YOUR_SCRIPTS+'*.d64')
    namesonly = []
    for file in filelist:
        namesonly.append(ntpath.basename(file))

    layout =  [
                [sg.Listbox(values=namesonly, size=(30, 19), select_mode=sg.SELECT_MODE_EXTENDED, key='demolist'), sg.Output(size=(88, 20), font='Courier 10')],
              #  [sg.Checkbox('verbose', default=False, key='verbose')],
                [sg.ReadFormButton('Write To Drive'), sg.ReadFormButton('Dump To Image'), sg.ReadFormButton('List'), sg.SimpleButton('EXIT')],
                ]

    form.Layout(layout)

    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = form.Read()
        if button in ('EXIT', None):
            break           # exit button clicked
        if button in ('ButtonTitle', 'ButtonTitle2'):
            print('Quickly launch your favorite programs using these shortcuts')
            print('Or  copy files to your github folder.  Or anything else you type on the command line')
            #Todo: execute commands
        elif button is 'Write To File':
            for index, file in enumerate(value['demolist']):
                form.Refresh()          # make the print appear immediately
                execute_command_blocking(LOCATION_OF_YOUR_SCRIPTS + file)


if __name__ == '__main__':
    Launcher2()


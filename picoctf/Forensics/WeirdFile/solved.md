# TITLE : Weird File
## Author : thelshell
## Description
What could go wrong if we let Word documents run programs? (aka "in-the-clear").
[weird.docm](https://challenge-files.picoctf.net/c_wily_courier/b5eb3574e45fb177ab55cdfa3cf81c79bfc87319bb87bec1cffe5fdd17b8fca9/weird.docm)
## Hints
- https://www.youtube.com/watch?v=Y7IJjnLGqTQ
## Solution
In this challenge, we are given a .docm file, which is a Microsoft Word document that contains VBA macros. To inspect the macro content without executing it, we can use tools such as olevba from the oletools suite.

The macro content can be extracted using the following command:
```
olevba <file_name>
```
The output:
```
FILE: weird.docm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file: word/vbaProject.bin - OLE stream: 'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Sub AutoOpen()
    MsgBox "Macros can run any program", 0, "Title"
    Signature

End Sub
 
 Sub Signature()
    Selection.TypeText Text:="some text"
    Selection.TypeParagraph
    
 End Sub
 
 Sub runpython()

Dim Ret_Val
Args = """" '"""
Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)
If Ret_Val = 0 Then
   MsgBox "Couldn't run python script!", vbOKOnly
End If
End Sub
+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |AutoOpen            |Runs when the Word document is opened        |
|Suspicious|Shell               |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|vbNormalFocus       |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|run                 |May run an executable file or a system       |
|          |                    |command                                      |
+----------+--------------------+---------------------------------------------+
```
From the output, we can see that the document contains an AutoOpen macro, which is automatically executed when the document is opened (if macros are enabled). The macro also defines a function named runpython() that uses the Shell() function to execute an external command.

Specifically, the macro runs a Python command that prints a Base64-encoded string:
```
cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9
```
After decoding this Base64 string, we obtain the flag. This confirms that the macro demonstrates the ability to execute external programs, which is a common technique abused by malicious documents, even though in this challenge it is used for educational purposes.


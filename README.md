<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module pacman</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>pacman</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:/Users/rebecarojas/Desktop/SemanaTec/SemanaTec/pacman.py">/Users/rebecarojas/Desktop/SemanaTec/SemanaTec/pacman.py</a></font></td></tr></table>
    <p><tt>Authors:&nbsp;Rebeca&nbsp;Rojas&nbsp;Pérez&nbsp;A01751192<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Juan&nbsp;Carlos&nbsp;Jiménez&nbsp;Tapia&nbsp;A01750115<br>
&nbsp;<br>
Pacman,&nbsp;classic&nbsp;arcade&nbsp;game.</tt></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-change"><strong>change</strong></a>(x, y)</dt><dd><tt>Change&nbsp;pacman&nbsp;aim&nbsp;if&nbsp;valid.</tt></dd></dl>
 <dl><dt><a name="-move"><strong>move</strong></a>()</dt><dd><tt>Move&nbsp;pacman&nbsp;and&nbsp;all&nbsp;ghosts.</tt></dd></dl>
 <dl><dt><a name="-offset"><strong>offset</strong></a>(point)</dt><dd><tt>Return&nbsp;offset&nbsp;of&nbsp;point&nbsp;in&nbsp;tiles.</tt></dd></dl>
 <dl><dt><a name="-square"><strong>square</strong></a>(x, y)</dt><dd><tt>Draw&nbsp;square&nbsp;using&nbsp;path&nbsp;at&nbsp;(x,&nbsp;y).</tt></dd></dl>
 <dl><dt><a name="-valid"><strong>valid</strong></a>(point)</dt><dd><tt>Return&nbsp;True&nbsp;if&nbsp;point&nbsp;is&nbsp;valid&nbsp;in&nbsp;tiles.</tt></dd></dl>
 <dl><dt><a name="-world"><strong>world</strong></a>()</dt><dd><tt>Draw&nbsp;world&nbsp;using&nbsp;path.</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>aim</strong> = vector(5, 0)<br>
<strong>ghosts</strong> = [[vector(-175, 160), vector(-10, 0)], [vector(-180, -170), vector(0, 10)], [vector(100, 80), vector(0, -10)], [vector(15, -160), vector(-10, 0)]]<br>
<strong>pacman</strong> = vector(30, -80)<br>
<strong>path</strong> = &lt;turtle.Turtle object&gt;<br>
<strong>state</strong> = {'score': 4}<br>
<strong>tiles</strong> = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...]<br>
<strong>writer</strong> = &lt;turtle.Turtle object&gt;</td></tr></table>
</body></html>
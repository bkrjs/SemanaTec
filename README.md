<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module memory</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>memory</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:/Users/rebecarojas/Desktop/SemanaTec/SemanaTec/memory.py">/Users/rebecarojas/Desktop/SemanaTec/SemanaTec/memory.py</a></font></td></tr></table>
    <p><tt>Authors:&nbsp;Authors:&nbsp;Rebeca&nbsp;Rojas&nbsp;Pérez&nbsp;A01751192<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Juan&nbsp;Carlos&nbsp;Jiménez&nbsp;Tapia&nbsp;A01750115<br>
Memory,&nbsp;puzzle&nbsp;game&nbsp;of&nbsp;number&nbsp;pairs.</tt></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-draw"><strong>draw</strong></a>()</dt><dd><tt>Draw&nbsp;image&nbsp;and&nbsp;tiles.</tt></dd></dl>
 <dl><dt><a name="-getrandbits"><strong>getrandbits</strong></a>(k, /)<font color="#909090"><font face="helvetica, arial"> method of <a href="random.html#Random">random.Random</a> instance</font></font></dt><dd><tt><a href="#-getrandbits">getrandbits</a>(k)&nbsp;-&gt;&nbsp;x.&nbsp;&nbsp;Generates&nbsp;an&nbsp;int&nbsp;with&nbsp;k&nbsp;random&nbsp;bits.</tt></dd></dl>
 <dl><dt><a name="-index"><strong>index</strong></a>(x, y)</dt><dd><tt>Convert&nbsp;(x,&nbsp;y)&nbsp;coordinates&nbsp;to&nbsp;tiles&nbsp;index.</tt></dd></dl>
 <dl><dt><a name="-random"><strong>random</strong></a>()<font color="#909090"><font face="helvetica, arial"> method of <a href="random.html#Random">random.Random</a> instance</font></font></dt><dd><tt><a href="#-random">random</a>()&nbsp;-&gt;&nbsp;x&nbsp;in&nbsp;the&nbsp;interval&nbsp;[0,&nbsp;1).</tt></dd></dl>
 <dl><dt><a name="-square"><strong>square</strong></a>(x, y)</dt><dd><tt>Draw&nbsp;white&nbsp;square&nbsp;with&nbsp;black&nbsp;outline&nbsp;at&nbsp;(x,&nbsp;y).</tt></dd></dl>
 <dl><dt><a name="-tap"><strong>tap</strong></a>(x, y)</dt><dd><tt>Update&nbsp;mark&nbsp;and&nbsp;hidden&nbsp;tiles&nbsp;based&nbsp;on&nbsp;tap.</tt></dd></dl>
 <dl><dt><a name="-xy"><strong>xy</strong></a>(count)</dt><dd><tt>Convert&nbsp;tiles&nbsp;count&nbsp;to&nbsp;(x,&nbsp;y)&nbsp;coordinates.</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>car</strong> = '/opt/anaconda3/lib/python3.8/site-packages/freegames/car.gif'<br>
<strong>hide</strong> = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, ...]<br>
<strong>state</strong> = {'mark': 27}<br>
<strong>taps</strong> = 2<br>
<strong>tiles</strong> = [27, 18, 16, 8, 11, 19, 20, 29, 24, 24, 5, 25, 7, 22, 1, 10, 30, 4, 7, 8, ...]</td></tr></table>
</body></html>
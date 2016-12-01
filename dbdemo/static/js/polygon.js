






(function (){
	
		
	var line_odd = $('<div class="lineF"> </div>');
	var line_even = $('<div class="lineS"> </div>');	
	var hexagon = $('<div class="boxF"> <div class="boxS"> <div class="boxT">   <div class="overlay"></div></div> </div> </div>');
	
	
	//get data
	
	
	
	
	
	
	var data = [{"name":"Sam Acho","team":"Chicago Bears","position":"OLB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AchoSa00.jpg","SUMMARY":"Career","AV":"24","Sk":"14.0","Tkl":"137","FF":"9"},{"name":"Kenneth Acker","team":"Kansas City Chiefs","position":"CB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AckeKe00.jpg","SUMMARY":"Career","AV":"5","Int":"3","Yds":"45","TD":"0"},{"name":"Jared Abbrederis","team":"","position":"WR","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AbbrJa00.jpg","SUMMARY":"Career","AV":"1","Rec":"10","Yds":"119","Y/R":"11.9","TD":"0","FantPt":"11.1"},{"name":"Ameer Abdullah","team":"Detroit Lions","position":"RB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AbduAm00.jpg","SUMMARY":"Career","AV":"5","Rush":"161","Yds":"698","Y/A":"4.3","TD":"2","FantPt":"92.0"},{"name":"Oday Aboushi","team":"Houston Texans","position":"OT","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AbouOd00.jpg","SUMMARY":"Career","AV":"6","GS":"16"},{"name":"Andrew Adams","team":"New York Giants","position":"S","SUMMARY":"Career","AV":"","GS":"8"},{"name":"Davante Adams","team":"Green Bay Packers","position":"WR","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AdamDa01.jpg","SUMMARY":"Career","AV":"9","Rec":"146","Yds":"1705","Y/R":"11.7","TD":"12","FantPt":"118.9"},{"name":"Jerell Adams","team":"New York Giants","position":"TE","SUMMARY":"Career","AV":"","Rec":"9","Yds":"74","Y/R":"8.2","TD":"1","FantPt":""},{"name":"Mike Adams","team":"Indianapolis Colts","position":"DB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AdamMi21.jpg","SUMMARY":"Career","AV":"53","Int":"23","Yds":"228","TD":"2"},{"name":"Mike Adams","team":"Chicago Bears","position":"OT","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AdamMi02.jpg","SUMMARY":"Career","AV":"11","GS":"21"},{"name":"Tyrell Adams","team":"Oakland Raiders","position":"LB","SUMMARY":"Career","AV":""},{"name":"Jahleel Addae","team":"San Diego Chargers","position":"S","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AddaJa00.jpg","SUMMARY":"Career","AV":"8","Sk":"3.0","Tkl":"148","FF":"3"},{"name":"Mario Addison","team":"Carolina Panthers","position":"DE","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AddiMa00.jpg","SUMMARY":"Career","AV":"8","Sk":"22.5","Tkl":"52","FF":"5"},{"name":"Nelson Agholor","team":"Philadelphia Eagles","position":"WR","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AghoNe00.jpg","SUMMARY":"Career","AV":"2","Rec":"50","Yds":"547","Y/R":"10.9","TD":"2","FantPt":"32.3"},{"name":"Roberto Aguayo","team":"Tampa Bay Buccaneers","position":"K","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AguaRo00.jpg","SUMMARY":"Career","AV":"","FGM":"13","FGA":"19","XPM":"22","XPA":"24"},{"name":"Kamar Aiken","team":"Baltimore Ravens","position":"WR","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AikeKa00.jpg","SUMMARY":"Career","AV":"9","Rec":"120","Yds":"1447","Y/R":"12.1","TD":"8","FantPt":"167.1"},{"name":"Walt Aikens","team":"Miami Dolphins","position":"CB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AikeWa00.jpg","SUMMARY":"Career","AV":"3","GS":"5"},{"name":"Jay Ajayi","team":"Miami Dolphins","position":"RB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AjayJa00.jpg","SUMMARY":"Career","AV":"2","Rush":"211","Yds":"1034","Y/A":"4.9","TD":"8","FantPt":"35.7"},{"name":"Branden Albert","team":"Miami Dolphins","position":"G","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlbeBr20.jpg","SUMMARY":"Career","AV":"47","GS":"113"},{"name":"D.J. Alexander","team":"Kansas City Chiefs","position":"OLB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlexD.00.jpg","SUMMARY":"Career","AV":"1"},{"name":"Dominique Alexander","team":"Cleveland Browns","position":"LB","SUMMARY":"Career","AV":""},{"name":"Kwon Alexander","team":"Tampa Bay Buccaneers","position":"OLB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlexKw00.jpg","SUMMARY":"Career","AV":"5","Sk":"6.0","Tkl":"134","FF":"2"},{"name":"Lorenzo Alexander","team":"Buffalo Bills","position":"DT","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlexLo99.jpg","SUMMARY":"Career","AV":"20","Sk":"19.0","Tkl":"156","FF":"6"},{"name":"Mackensie Alexander","team":"Minnesota Vikings","position":"CB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlexMa01.jpg","SUMMARY":"Career","AV":""},{"name":"Maurice Alexander","team":"Los Angeles Rams","position":"SS","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlexMa00.jpg","SUMMARY":"Career","AV":"4","Sk":"3.0","Tkl":"58","FF":"0"},{"name":"Vadal Alexander","team":"Oakland Raiders","position":"OG","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlexVa00.jpg","SUMMARY":"Career","AV":"","GS":"2"},{"name":"Robert Alford","team":"Atlanta Falcons","position":"CB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlfoRo00.jpg","SUMMARY":"Career","AV":"12","Int":"9","Yds":"131","TD":"2"},{"name":"Antonio Allen","team":"New York Jets","position":"SS","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlleAn02.jpg","SUMMARY":"Career","AV":"9","Sk":"2.5","Tkl":"77","FF":"1"},{"name":"Beau Allen","team":"Philadelphia Eagles","position":"DT","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlleBe00.jpg","SUMMARY":"Career","AV":"3","GS":"5"},{"name":"Dwayne Allen","team":"Indianapolis Colts","position":"TE","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlleDw00.jpg","SUMMARY":"Career","AV":"8","Rec":"115","Yds":"1301","Y/R":"11.3","TD":"15","FantPt":"183.1"},{"name":"Javorius Allen","team":"Baltimore Ravens","position":"RB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlleJa01.jpg","SUMMARY":"Career","AV":"5","Rush":"146","Yds":"548","Y/A":"3.8","TD":"1","FantPt":"100.7"},{"name":"Jeff Allen","team":"Houston Texans","position":"T","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlleJe01.jpg","SUMMARY":"Career","AV":"15","GS":"46"},{"name":"Keenan Allen","team":"San Diego Chargers","position":"WR","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlleKe00.jpg","SUMMARY":"Career","AV":"21","Rec":"221","Yds":"2617","Y/R":"11.8","TD":"16","FantPt":"341.4"},{"name":"Nate Allen","team":"Oakland Raiders","position":"DB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlleNa99.jpg","SUMMARY":"Career","AV":"29","Int":"11","Yds":"164","TD":"0"},{"name":"Ricardo Allen","team":"Atlanta Falcons","position":"CB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlleRi00.jpg","SUMMARY":"Career","AV":"6","Int":"4","Yds":"13","TD":"0"},{"name":"Ryan Allen","team":"New England Patriots","position":"P","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlleRy01.jpg","SUMMARY":"Career","AV":"7"},{"name":"Geronimo Allison","team":"Green Bay Packers","position":"WR","SUMMARY":"Career","AV":"","Rec":"3","Yds":"38","Y/R":"12.7","TD":"1","FantPt":""},{"name":"Kiko Alonso","team":"Miami Dolphins","position":"ILB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AlonKi00.jpg","SUMMARY":"Career","AV":"11","Int":"7","Yds":"108","TD":"1"},{"name":"Tyson Alualu","team":"Jacksonville Jaguars","position":"DT","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AluaTy99.jpg","SUMMARY":"Career","AV":"35","Sk":"17.5","Tkl":"166","FF":"1"},{"name":"Jace Amaro","team":"Tennessee Titans","position":"TE","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AmarJa00.jpg","SUMMARY":"Career","AV":"3","Rec":"41","Yds":"404","Y/R":"9.9","TD":"2","FantPt":"46.5"},{"name":"Danny Amendola","team":"New England Patriots","position":"WR","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AmenDa00.jpg","SUMMARY":"Career","AV":"28","Rec":"362","Yds":"3420","Y/R":"9.4","TD":"17","FantPt":"399.0"},{"name":"David Amerson","team":"Oakland Raiders","position":"CB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AmerDa00.jpg","SUMMARY":"Career","AV":"14","Int":"8","Yds":"73","TD":"2"},{"name":"Adrian Amos","team":"Chicago Bears","position":"FS","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AmosAd00.jpg","SUMMARY":"Career","AV":"6","GS":"27"},{"name":"Prince Amukamara","team":"Jacksonville Jaguars","position":"CB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AmukPr00.jpg","SUMMARY":"Career","AV":"18","Int":"7","Yds":"68","TD":"0"},{"name":"C.J. Anderson","team":"Denver Broncos","position":"RB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AndeC.00.jpg","SUMMARY":"Career","AV":"15","Rush":"448","Yds":"2044","Y/A":"4.6","TD":"17","FantPt":"297.4"},{"name":"Colt Anderson ","team":"Buffalo Bills","position":"DB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AndeCo01.jpg","SUMMARY":"Career","AV":"7","GS":"7"},{"name":"Derek Anderson ","team":"Carolina Panthers","position":"QB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AndeDe00.jpg","SUMMARY":"Career","AV":"20","QBrec":"20-26-0","Cmp%":"54.2","Yds":"10396","Y/A":"6.5","TD":"60","Int":"59","FantPt":"553.3"},{"name":"Henry Anderson","team":"Indianapolis Colts","position":"DE","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AndeHe00.jpg","SUMMARY":"Career","AV":"4","GS":"9"},{"name":"Jonathan Anderson","team":"Chicago Bears","position":"LB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AndeJo01.jpg","SUMMARY":"Career","AV":"2","GS":"3"},{"name":"Robby Anderson","team":"New York Jets","position":"WR","SUMMARY":"Career","AV":"","Rec":"24","Yds":"304","Y/R":"12.7","TD":"0","FantPt":""},{"name":"Stephen Anderson","team":"Houston Texans","position":"TE","SUMMARY":"Career","AV":"","Rec":"10","Yds":"86","Y/R":"8.6","TD":"1","FantPt":""},{"name":"Zaire Anderson","team":"Denver Broncos","position":"LB","SUMMARY":"Career","AV":""},{"name":"Antonio Andrews","team":"Tennessee Titans","position":"RB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AndrAn00.jpg","SUMMARY":"Career","AV":"4","Rush":"145","Yds":"535","Y/A":"3.7","TD":"3","FantPt":"92.1"},{"name":"David Andrews","team":"New England Patriots","position":"C","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AndrDa00.jpg","SUMMARY":"Career","AV":"7","GS":"22"},{"name":"Josh Andrews","team":"Philadelphia Eagles","position":"G","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AndrJo01.jpg","SUMMARY":"Career","AV":"1"},{"name":"Bryan Anger","team":"Tampa Bay Buccaneers","position":"P","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AngeBr00.jpg","SUMMARY":"Career","AV":"12"},{"name":"Ezekiel Ansah","team":"Detroit Lions","position":"DE","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AnsaEz00.jpg","SUMMARY":"Career","AV":"27","Sk":"30.0","Tkl":"107","FF":"9"},{"name":"Stephone Anthony","team":"New Orleans Saints","position":"ILB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/AnthSt00.jpg","SUMMARY":"Career","AV":"6","GS":"18"},{"name":"Eli Apple","team":"New York Giants","position":"CB","img":"https://d395i9ljze9h3x.cloudfront.net/req/20160913/images/headshots/ApplEl00.jpg","SUMMARY":"Career","AV":"","GS":"6"}];
	
	var n = (data.length / 13) * 2 ; 
	
		for (var i = 0; i < 52;  i++) {
				var boxF = $('<div class="boxF">  </div>');
				var boxS = $('<div class="boxS">   </div>');
				var boxT = $('<div class="boxT"> </div>');

				var icon_url =  data[i ]['img'];
				boxT.attr('style', 'background-image:url(' +  icon_url +  ')' );
				
				var overlay =  data[i]['Free'] ?   $('<div class="overlay free" >   </div> ') : 
				$('<div class="overlay" name=' +   data[i]["name"]  + 'team=' + data[i]['team']      +   ' >  </div> '  );
				
				
// 				
				
				
				//var info_position = 'top:' + 58.24 * i +  'px; ' +   'left:' + 33.6 * (i % 2) +  'px;'    ;
				//var li = $('<li> </li>');
				
				
	
				//info.attr('style', info_position);	
				boxT.append(overlay);			
				boxS.append(boxT);
				boxF.append(boxS);
		
				
				$('#hive').append($('<li> </li>').append(boxF)); 
				
				

				
				
		
			
		
		}
	
	
	
	
	
	
	
	$('.overlay').hover(function(){
	  
	  
	  var details = '<h4>' +  $(this).attr('name') +  '</h4> ';
	  
	  $('.info_wrapper').html(details);
	  
	  
	});
	
	
	
	
	
	

}) ();






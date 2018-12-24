
//import {PythonShell} from 'python-shell';
function get_scrape() {
	
let {PythonShell} = require('python-shell')	
//var PythonShell = require("python-shell")
var path = require("path")

var options = {
scriptPath : path.join(__dirname,'/../Jo_Engine/')
}

let scrape = new PythonShell('job_module.py',options);

scrape.on('message',function(message){
swal(message,"success");
})

}
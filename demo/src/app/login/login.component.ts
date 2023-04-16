import { Component } from '@angular/core';
import {PcServiceService} from "../pc-service.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent{
  logged:boolean = false
  username:string = ""
  password:string = ""
  constructor(private pcservice:PcServiceService){}
  ngOnInit(){
    const token = localStorage.getItem('token');
    if (token){
      this.logged=true;
    }
  }
  login(){
    this.pcservice.login(this.username, this.password).subscribe((data)=>{
      localStorage.setItem('token', data.token);
      this.logged=true;
    })
  }
  logout(){
    localStorage.removeItem('token');
    this.logged = false;
    this.username = "";
    this.password = "";
  }
}

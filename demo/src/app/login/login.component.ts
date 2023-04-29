import { Component } from '@angular/core';
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent{
  username:string = ""
  password:string = ""
  constructor(public auth:AuthService){}
  ngOnInit(){
  }
  login(){
    this.auth.login(this.username, this.password).subscribe((data)=>{
      localStorage.setItem('token', data.token);
      this.auth.isAuth=true;
    })
  }
  logout(){
    localStorage.removeItem('token');
    this.auth.isAuth = false;
    this.username = "";
    this.password = "";
  }
}

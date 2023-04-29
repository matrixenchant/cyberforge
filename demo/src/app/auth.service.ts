import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  BASE_URL = 'http://127.0.0.1:8000'
  isAuth:boolean = false;
  constructor(private client:HttpClient) {
    const token = localStorage.getItem('token');
    if (token){
      this.isAuth=true;
    }
  }
  login(username:string, password:string):Observable<AuthToken>{
    return this.client.post<AuthToken>(`${this.BASE_URL}/users/login/`, {username, password});
  }
}

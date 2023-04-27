import { Injectable } from '@angular/core';
import { HttpClient, HttpXsrfTokenExtractor } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class ApiService {
  constructor(
    private http: HttpClient,
    private tokenExtractor: HttpXsrfTokenExtractor
  ) {}

  logout(): Observable<any> {
    const csrfToken = this.tokenExtractor.getToken() as string;
    const headers = {
      'X-CSRFToken': csrfToken
    };
    return this.http.post('/users/logout/', {}, { headers });
  }
}

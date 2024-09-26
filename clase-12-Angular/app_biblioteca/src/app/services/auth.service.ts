import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, take } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url = '/api';
  constructor(
    private httpClient: HttpClient,
    private router: Router
  ) { }


  login(dataLogin:any): Observable<any> {
    // let dataLogin = {
    //   email : "rodrigo.bartolome@um.edu.ar",
    //   password : "123456"
    // }
    return this.httpClient.post(this.url+'/auth/login',dataLogin).pipe(take(1));
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigateByUrl('home');
  }
}

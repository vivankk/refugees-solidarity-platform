import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private baseUrl = 'http://localhost:5000/';
  private newUserUrl = this.baseUrl + 'add_user';

  constructor(private http: HttpClient) { }

  add_user(userProps: Object) {
    return this.http.post(this.newUserUrl, userProps);
  }

}

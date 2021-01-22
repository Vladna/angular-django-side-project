import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Knjige } from '../models/Knjige';

@Injectable({
  providedIn: 'root'
})
export class KnjigeService {
  //ASP.NET API URL
  // private readonly APIUrl = "http://localhost:62808/api";
  //Python API URL   

  /*  constructor(private http: HttpClient) {
 
   }
 
   getKnjige(): Observable<any[]> {
     return this.http.get<any>(this.APIUrl + '/Knjiga');
   }
   addKnjiga(knjiga: Knjige) {
     return this.http.post(this.APIUrl + '/Knjiga', knjiga);
   }
   updateKnjiga(knjiga: Knjige) {
     return this.http.put(this.APIUrl + '/Knjiga', knjiga);
   }
   deleteKnjiga(id: number) {
     return this.http.delete(this.APIUrl + '/Knjiga/' + id);
   }
   UploadPhoto(val: any) {
     return this.http.post(this.APIUrl + '/Knjiga/SaveFile', val);
   }
   getAllSlobodneKnjige(): Observable<Knjige[]> {
     return this.http.get<any>(this.APIUrl + '/Knjiga/NaStanju');
 
   }
   getKnjigeNaStanju(): Observable<any[]> {
     return this.http.get<any>(this.APIUrl + '/Knjiga/NaStanju');
   }
   getKnjigaEdit(id: number): Observable<Knjige[]> {
     return this.http.get<any>(this.APIUrl + "/Knjiga/KnjigaEdit/" + id);
   } */
  private readonly APIUrl = "http://127.0.0.1:8000/";
  constructor(private http: HttpClient) {

  }

  getKnjige(): Observable<any[]> {
    return this.http.get<any>(this.APIUrl + 'knjige/');
  }
  addKnjiga(knjiga: Knjige) {
    return this.http.post(this.APIUrl + 'knjige/', knjiga);
  }
  updateKnjiga(knjiga: Knjige) {
    return this.http.put(this.APIUrl + 'knjige/', knjiga);
  }
  deleteKnjiga(id: number) {
    return this.http.delete(this.APIUrl + 'knjige/' + id);  
  }
  UploadPhoto(val: any) {
    return this.http.post(this.APIUrl + 'knjige/SaveFile', val);
  }
  getAllSlobodneKnjige(): Observable<Knjige[]> {
    return this.http.get<any>(this.APIUrl + 'knjige/NaStanju');

  }
  getKnjigeNaStanju(): Observable<any[]> {
    return this.http.get<any>(this.APIUrl + 'knjige/NaStanju');
  }
  getKnjigaEdit(id: number): Observable<Knjige[]> {
    return this.http.get<any>(this.APIUrl + "knjige/KnjigaEdit/" + id);
  }
}

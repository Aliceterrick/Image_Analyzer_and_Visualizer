import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ImageResult } from '../models/image-result';

@Injectable({ providedIn: 'root' })
export class ResultsService {
  private apiUrl = 'http://localhost:5102/api/results';

  constructor(private http: HttpClient) {}

  listKeys(): Observable<string[]> {
    return this.http.get<string[]>(this.apiUrl);
  }

  getResult(key: string): Observable<ImageResult> {
    return this.http.get<ImageResult>(`${this.apiUrl}/${key}`);
  }
}

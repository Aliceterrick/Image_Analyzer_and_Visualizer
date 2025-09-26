import { Routes } from '@angular/router';
import { ResultsComponent } from './components/results/results.component';

export const routes: Routes = [
  { path: '', component: ResultsComponent },
  { path: 'results', component: ResultsComponent }
];
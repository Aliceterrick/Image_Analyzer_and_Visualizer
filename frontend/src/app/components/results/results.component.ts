import { Component, OnInit } from '@angular/core';
import { NgIf, NgFor, PercentPipe } from '@angular/common';
import { ResultsService } from '../../services/results.service';
import { ImageResult } from '../../models/image-result';


@Component({
  selector: 'app-results',
  standalone: true,
  imports: [NgIf, NgFor, PercentPipe],
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.scss']
})
export class ResultsComponent implements OnInit {
  keys: string[] = [];
  selected?: ImageResult;

  constructor(private resultsService: ResultsService) {}

  ngOnInit(): void {
    this.resultsService.listKeys().subscribe((data: string[]) => this.keys = data);
  }

  loadResult(key: string): void {
    this.resultsService.getResult(key).subscribe((data: ImageResult) => this.selected = data);
  }

  getOriginalUrl(): string {
    return `http://localhost:5102/data/images/${this.selected?.image}`;
  }

  getAnnotatedUrl(type: 'cloud' | 'local'): string {
    const id = this.selected?.image.replace('.jpg', '');
    return `http://localhost:5102/data/annotated_images/${type}_annotated_${id}.jpg`;
  }
}

